
import openneuro as on
import os

class OpenNeuroDataSet:
  def __init__(self):
    """
    Initialize 
    """

  def download(self, dataset_id, target_dir='data'):
    """
    Download the specified dataset to the target directory.
    """

    try:
      if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        on.download(dataset=dataset_id, target_dir=target_dir)

    except Exception as e:
      print(f"An error occured while downloading the dataset: {e}")

  def display(self):
    """
    identify and list all neuroimaging recording filenames
    """ 

      
  def process(self):
    """
    Process and format data into the proper file structure
    """
  
  def parse_event(self):
    """
    - Develop a method to parse and list the 'events' in each recording (e.g., images, sounds).
    - Include columns for event types and their relative onsets in the recordings.
    """
    

