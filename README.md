# Context Tags

A practical technique for managing code context when working with Large Language Models. Context Tags helps developers retrieve relevant code segments through tag-based searches, making it easier to provide focused, efficient context during LLM interactions.

## Overview

Context Tags works with a JSON-based knowledge graph of your codebase. Using an interactive CLI, you can search for code segments by tags, retrieve related components, and easily copy the results into LLM chat windows. Context Tags supports multiple approaches to code discovery - from traditional tag matching to vector databases for semantic search and graph databases for relationship exploration.

## Features

- Tag-based code segment retrieval
- Interactive command line interface
- Smart tag suggestions
- Copy-paste friendly output
- Knowledge graph integration
- Related code discovery

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/brandondocusen/contexttags.git
cd contexttags
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Place your knowledge graph file in the project directory as `knowledge-graph-cumulative.json`. A sample knowledge graph is provided.

4. Run the interactive CLI:
```bash
python contexttags.py
```

5. Search using tags:
- Enter tags separated by commas (e.g., "String, Logger")
- Type 'tags' to see all available tags
- Type 'help' for usage information
- Type 'quit' or press Ctrl+C to exit

## Sample Usage

```bash
> Enter tags (comma-separated) or command: String, Logger
Found 2 elements matching ALL tags: String, Logger
...
```

## Knowledge Graph Structure

The knowledge graph (`knowledge-graph-cumulative.json`) should follow this format:
```json
[
  {
    "Module": "ModuleName",
    "Tags": ["tag1", "tag2"],
    "Content": {
      "description": "Module description",
      "methods": [],
      "dependencies": []
    }
  }
]
```

## Requirements

- Python 3.8 or higher
- colorama package
- JSON-formatted knowledge graph

## Contributing

Contributions are welcome. Please read CONTRIBUTING.md for guidelines.

## Getting Help

- Review the documentation in the /docs folder
- Check existing issues or create a new one
- Read the sample knowledge graph for tag examples

## License

MIT License - See LICENSE file for details.

---
Author: Brandon Docusen  
Version: 1.0.0  
Status: Beta Release
