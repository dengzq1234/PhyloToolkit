# TreeGenerator

`TreeGenerator` is a command-line tool for generating random phylogenetic trees. It allows you to create trees either based on a provided list of species names or by specifying a number of species. The trees can be generated using different models (`yule` or `uniform`), and the resulting tree can be saved to a file.

## Requirements

- Python >= 3.10
- `ete4` library

You can install the required library using:

```bash
pip install https://github.com/etetoolkit/ete/archive/ete4.zip
```

## Installation
You can install it from github repo

```
git clone https://github.com/dengzq1234/TreeGenerator.git

cd TreeGenerator/

# Make the Script Executable
chmod +x treegenerator.py

# Add the TreeGenerator to Your PATH 
export PATH=$PATH:/path/to/TreeGenerator
```

## Usage

The script provides several options to customize the tree generation process. Below are the details of the available arguments.

### Arguments

- `-n`, `--number`: Number of species.
- `-l`, `--name-list`: Path to a file containing a list of species names (one per line).
- `-m`, `--model`: Random tree model (`yule` or `uniform`). Default is `yule`.
- `-o`, `--output`: Output filename. This argument is required.

### Example Commands

#### Generate a Tree with a Specified Number of Species

To generate a tree with a specified number of species using the default model (`yule`), run:

```bash
python treegenerator.py -n 5 -o output_tree.txt
```

This will create a tree with 5 species and save it to `output_tree.txt`.

#### Generate a Tree from a List of Species Names

To generate a tree from a provided list of species names, first create a file (e.g., `species_names.txt`) with each species name on a new line:

```
Taxa_A
Taxa_B
Taxa_C
```

Then, run:

```bash
python treegenerator.py -l species_names.txt -o output_tree.txt
```

This will create a tree using the species names from `species_names.txt` and save it to `output_tree.txt`.

#### Specify the Model

You can specify the model to use for generating the tree (`yule` or `uniform`). For example, to use the `uniform` model:

```bash
python treegenerator.py -n 5 -m uniform -o output_tree.txt
```

## Script Details

The script performs the following steps:

1. **Parse Arguments**: Parses the command-line arguments to determine the number of species, list of species names, model, and output filename.
2. **Generate Tree**:
   - If a list of names is provided, it reads the names from the file.
   - If a number is provided, it generates a list of names as `Taxa_0`, `Taxa_1`, etc.
   - Based on the provided model (`yule` or `uniform`), it generates a random tree.
3. **Save Tree**: Saves the generated tree to the specified output file.

## Example Usage

Here are some example commands and their expected outputs:

### Generate a Tree with 5 Species (Yule Model)

```bash
python treegenerator.py -n 5 -o output_tree.txt
```

### Generate a Tree from a List of Names (Uniform Model)

```bash
python treegenerator.py -l species_names.txt -m uniform -o output_tree.txt
```

### List of Species Names File (`species_names.txt`)

```
Taxa_A
Taxa_B
Taxa_C
Taxa_D
Taxa_E
```

### Command

```bash
python treegenerator.py -l species_names.txt -o output_tree.txt
```

This command will generate a tree using the names from `species_names.txt` and save it to `output_tree.txt`.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
