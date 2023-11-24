"""Module containing utility functions for the project"""
import os
import requests

# Create folder for models
def create_folder(folder_name: str) -> None:
    """Create folder with the specified given name

    Args:
        folder_name (str): The name of the folder to create
    """
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def download_model(url: str, folder_name: str, file_name: str) -> None:
    """Download model from url and save it to the folder with the specified given name

    Args:
        url (str): The URL of the model to download
        folder_name (str): The name of the folder to save the model to
        file_name (str): The name of the model file
    """
    # Check if the folder already exists
    if os.path.exists(folder_name):
        print(f"Folder '{folder_name}' already exists. Skipping download.")
        return

    # Create folder
    create_folder(folder_name)

    # Download model, timeout after 1 hour
    print(f"Downloading model from '{url}'...")
    response = requests.get(url, timeout=3600)
    if response.status_code == 200:
        # Save model with the determined filename
        with open(os.path.join(folder_name, file_name), 'wb') as file:
            file.write(response.content)
        print(f"Model saved successfully as '{file_name}'.")
    else:
        print(f"Error downloading model. Status code: {response.status_code}")
        return

    # Verify if files exist in the folder
    files_in_folder = os.listdir(folder_name)
    if not files_in_folder:
        print(f"No files found in '{folder_name}'. Download may have failed.")
        os.rmdir(folder_name)
        return
