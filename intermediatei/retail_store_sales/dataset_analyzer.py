class DataSet():
    # __init__() function to assign values to object attrs, or other operations that are necessary to do when the object is being created.
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None # Data not yet loaded, but variable initialized
        
    def load_data(self):
        self.data = pd.read_csv(self.file_path)  # Now self.data is a DataFrame
        
    def get_summary_statistics(self):
        if self.data is None:
            return "Data not loaded. Please call load_data() first."
        return self.data.describe()
    
class DataAnalyzer():
    def __init__(self):
        self.data_set = DataSet()