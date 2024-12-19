# Context Tags

An efficient technique for managing code context when working with Large Language Models. Context Tags retrieve only the relevant code segments of your code base through tag-based searches, making it easier to provide focused, efficient context during LLM interactions.

## Overview

Search for code segments by categorical tags or by granular code element names, retrieve related components, and easily copy the results into LLM chat windows. Context Tags supports multiple approaches to code discovery - from traditional tag matching to vector databases for semantic search and graph databases for relationship exploration.

## Features

- Tag-based code segment retrieval
- Interactive command line interface
- Smart tag suggestions
- Copy-paste friendly output
- Knowledge graph integration
- Related code discovery

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
