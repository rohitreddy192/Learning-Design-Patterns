class SortingStrategy:
    def sort(self, data):
        pass

class BubbleSort(SortingStrategy):
    def sort(self,data):
        print("Inside Bubble Sort")
        ## Bubble Sort Algorithm goes here
        return sorted(data) 
    
class MergeSort(SortingStrategy):
    def sort(self, data):
        print("Inside Merge Sort")
        ## Merge Sort Algorithm goes here
        return sorted(data)

###########################################################################################
######  We can add any number of Sorting algorithms, That wont affect the client code. ####  
###### This runtime switching in algorithms is provided by Strategy Design Pattern ########
###########################################################################################
class SortContext:
    def __init__(self,strategy):
        self.strategy = strategy
    def set_strategy(self, strategy):
        self.strategy = strategy
    def execute_sort(self,data):
        return self.strategy.sort(data)
    

if __name__ == "__main__":
    data_to_sort = [5,4,1,3,2]
    context = SortContext(BubbleSort())
    sorted_data = context.execute_sort(data_to_sort)
    print("After Bubble Sort:")
    for i in sorted_data:
        print(i, end = ' ')
    print()
    context.set_strategy(MergeSort())
    sorted_data = context.execute_sort(data_to_sort)
    print("After Merge Sort:")
    for i in sorted_data:
        print(i, end = ' ')