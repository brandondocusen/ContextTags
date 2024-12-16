"""
Context Tags - A tool for managing context windows in LLM-assisted development
Copyright (c) 2024 Brandon Docusen
Homepage: https://github.com/brandondocusen/contexttags

This tool helps developers efficiently manage context windows for Large Language Models
by retrieving relevant code segments through tag-based searches of a project's knowledge graph.

MIT License - You are free to:
- Use this commercially
- Modify this code
- Distribute this code
- Use this privately
- Sublicense this code

While maintaining the original copyright notice and license.

Original author: Brandon Docusen
Contact: b.docusen@me.com
Contribute: https://github.com/brandondocusen/contexttags
"""


import json
import sys
import colorama
from colorama import Fore, Style
from typing import List, Dict, Set
import textwrap
import os

def load_knowledge_graph(file_path: str) -> List[Dict]:
    """Load and parse the JSON knowledge graph file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Could not find file at {file_path}{Style.RESET_ALL}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Invalid JSON file{Style.RESET_ALL}")
        sys.exit(1)

def get_all_tags(knowledge_graph: List[Dict]) -> Set[str]:
    """Extract all unique tags from the knowledge graph."""
    tags = set()
    for element in knowledge_graph:
        tags.update(element.get("Tags", []))
    return tags

def find_matching_elements(knowledge_graph: List[Dict], search_tags: List[str]) -> List[Dict]:
    """Find elements that match ALL of the provided tags."""
    matching_elements = []
    search_tags_set = set(tag.lower() for tag in search_tags)
    
    for element in knowledge_graph:
        element_tags = set(tag.lower() for tag in element.get("Tags", []))
        if all(tag in element_tags for tag in search_tags_set):
            matching_elements.append(element)
    return matching_elements

def display_element(element: Dict) -> None:
    """Format and display a single element."""
    print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Module: {Fore.WHITE}{element['Module']}")
    print(f"{Fore.CYAN}Tags: {Fore.WHITE}{', '.join(element['Tags'])}")
    print(f"{Fore.CYAN}Content:{Style.RESET_ALL}")
    
    content = element['Content']
    
    # Display description with proper wrapping
    description = content.get('description', 'N/A')
    print(f"- {Fore.YELLOW}Description:{Style.RESET_ALL}")
    for line in textwrap.wrap(description, width=76):
        print(f"  {line}")
    
    # Display methods with descriptions
    if 'methods' in content and content['methods']:
        print(f"\n- {Fore.YELLOW}Methods:{Style.RESET_ALL}")
        for method in content['methods']:
            method_name = method.get('method', 'Unknown')
            method_desc = method.get('description', 'No description available')
            print(f"  {Fore.GREEN}• {method_name}:{Style.RESET_ALL}")
            for line in textwrap.wrap(method_desc, width=74):
                print(f"    {line}")
    
    # Display dependencies
    if 'dependencies' in content and content['dependencies']:
        deps_str = ', '.join(content['dependencies'])
        print(f"\n- {Fore.YELLOW}Dependencies:{Style.RESET_ALL}")
        for line in textwrap.wrap(deps_str, width=76):
            print(f"  {line}")

def suggest_related_tags(all_tags: Set[str], current_tags: List[str], max_suggestions: int = 5) -> List[str]:
    """Suggest related tags based on common prefixes and patterns."""
    current_tags_set = set(tag.lower() for tag in current_tags)
    suggestions = []
    
    for tag in all_tags:
        if tag.lower() not in current_tags_set:
            # Suggest tags that share prefixes with current tags
            for current_tag in current_tags:
                if (tag.startswith(current_tag) or current_tag.startswith(tag) or
                    any(word in tag for word in current_tag.split()) or
                    any(word in current_tag for word in tag.split())):
                    suggestions.append(tag)
                    break
    
    return suggestions[:max_suggestions]

def print_welcome_message():
    """Display the welcome message and instructions."""
    print(f"{Fore.CYAN}{'='*80}")
    print("Context Tagging System - Code Discovery Tool")
    print("='*80")
    print(f"\n{Fore.WHITE}This tool helps you discover relevant code segments using tags.")
    print("Commands:")
    print("  - Enter tags separated by commas")
    print("  - Type 'tags' to see all available tags")
    print("  - Type 'help' for this message")
    print("  - Type 'quit', '/q', or press Ctrl+C to exit")
    print(f"{Fore.CYAN}{'='*80}{Style.RESET_ALL}\n")

def main():
    # Initialize colorama
    colorama.init()

    # Path to the knowledge graph file
    file_path = "knowledge-graph-cumulative.json"
    
    # Load the knowledge graph
    knowledge_graph = load_knowledge_graph(file_path)
    
    # Get all available tags
    all_tags = get_all_tags(knowledge_graph)
    
    # Print welcome message
    print_welcome_message()
    
    # Main interaction loop
    while True:
        try:
            user_input = input(f"\n{Fore.GREEN}Enter tags (comma-separated) or command: {Style.RESET_ALL}").strip()
            
            # Handle exit commands
            if user_input.lower() in ['quit', '/q', 'exit']:
                print(f"\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
                break
            
            # Handle help command
            if user_input.lower() == 'help':
                print_welcome_message()
                continue
            
            # Handle tags command
            if user_input.lower() == 'tags':
                print(f"\n{Fore.YELLOW}Available tags:{Style.RESET_ALL}")
                sorted_tags = sorted(all_tags)
                for i, tag in enumerate(sorted_tags):
                    print(f"{tag:<30}", end='\n' if (i + 1) % 3 == 0 else '')
                print("\n")
                continue
            
            # Process tag search
            search_tags = [tag.strip() for tag in user_input.split(',') if tag.strip()]
            
            if not search_tags:
                print(f"{Fore.RED}Error: No valid tags provided{Style.RESET_ALL}")
                continue
            
            # Find and display matching elements
            matching_elements = find_matching_elements(knowledge_graph, search_tags)
            
            if not matching_elements:
                print(f"\n{Fore.RED}No elements found matching ALL tags: {', '.join(search_tags)}{Style.RESET_ALL}")
                
                # Suggest related tags
                suggestions = suggest_related_tags(all_tags, search_tags)
                if suggestions:
                    print(f"\n{Fore.YELLOW}Suggested related tags:{Style.RESET_ALL}")
                    print(', '.join(suggestions))
            else:
                print(f"\n{Fore.GREEN}Found {len(matching_elements)} elements matching ALL tags: {', '.join(search_tags)}{Style.RESET_ALL}")
                
                for element in matching_elements:
                    display_element(element)
                
                # Show separator after results
                print(f"\n{Fore.CYAN}{'='*80}{Style.RESET_ALL}")
        
        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}Goodbye!{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()