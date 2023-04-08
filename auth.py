import getpass
import yaml
import sys

def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.yaml'

    # Load the config.yaml file
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Prompt the user to enter the OpenAI and HuggingFace keys
    print("Enter your OpenAI key:")
    openai_key = getpass.getpass()
    print("Enter your HuggingFace token:")
    huggingface_key = getpass.getpass()

    # Update the values in the config dictionary
    config['openai']['key'] = openai_key
    config['huggingface']['token'] = huggingface_key

    # Save the updated config back to the file
    with open(config_path, 'w') as file:
        yaml.safe_dump(config, file)

if __name__ == '__main__':
    main()
