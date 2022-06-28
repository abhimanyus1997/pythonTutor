# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="day17_module.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

# Creating an object
logger = logging.getLogger(__name__)
list_logger = logging.getLogger("list_Log")
dict_logger = logging.getLogger("dict_Log")

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
list_logger.setLevel(logging.DEBUG)
dict_logger.setLevel(logging.DEBUG)

# Test messages
logger.info("logger Ready")
list_logger.info("list logger Ready")
dict_logger.info("dict logger Ready")


## USER DEFINED LIST CLASS
try:
    class mylist:
        try:
            def __init__(self,mylist) -> None:
                # Type checking of user input paramater for constructor
                if type(mylist) != list:
                    raise TypeError("Class paramater is not a List")
                    list_logger.warning(f"Class paramater passed is of type {type(mylist)}")
                self.mylist = mylist
                list_logger.info(f"Created self.mylist as {self.mylist}")
        except Exception as e:
            list_logger.error(f"Error occured during Class initialization: {e}")


        try:
            def append(self,element) -> None:
                """Adds an element at the end of the list"""
                try:
                    list_logger.info(f"Using append method with parameter: element={element}")
                    return self.mylist.append(element)
                except Exception as e:
                    list_logger.error(f"Error occured inside Append Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at Append Method: {e}")


        try:
            def clear(self) -> None:
                """Removes all the elements from a list"""
                try:
                    list_logger.info(f"Using clear method")
                    return self.mylist.clear()
                except Exception as e:
                    list_logger.error(f"Error occured inside clear Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at clear Method: {e}")

        try:
            def copy(self) -> list:
                """Returns a copy of the specified list."""
                try:
                    list_logger.info(f"Using copy method")
                    return self.mylist.copy()
                except Exception as e:
                    list_logger.error(f"Error occured inside copy Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at copy Method: {e}")


        try:
            def count(self,value) -> int:
                """Returns the number of elements with the specified value"""
                try:
                    list_logger.info(f"Using count method with parameter: value={value}")
                    return self.mylist.count(value)
                except Exception as e:
                    list_logger.error(
                        f"Error occured inside count Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at count Method: {e}")


        try:
            def extend(self,iterable) -> list:
                """Add the elements of a list (or any iterable), to the end of the current list"""
                try:
                    list_logger.info(f"Using extend method with parameter: iterable={iterable}")
                    return self.mylist.extend(iterable)
                except Exception as e:
                    list_logger.error(f"Error occured inside extend Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at extend Method: {e}")



        try:
            def index(self,elmnt) -> int:
                """Returns the index of the first element with the specified value"""
                try:
                    list_logger.info(f"Using index method with parameter: element={elmnt}")
                    return self.mylist.index(elmnt)
                except Exception as e:
                    list_logger.error(f"Error occured inside index Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at index Method: {e}")



        try:
            def insert(self,pos, elmnt) -> list:
                """Adds an element at the specified position"""
                try:
                    list_logger.info(f"Using insert method with parameters: position={pos} & element={elmnt}")
                    return self.mylist.insert(pos, elmnt)
                except Exception as e:
                    list_logger.error(f"Error occured inside insert Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at insert Method: {e}")



        try:
            def pop(self,pos = -1):
                """Removes the element at the specified position"""
                try:
                    list_logger.info(f"Using pop method with parameter: position={pos}")
                    return self.mylist.pop(pos)
                except Exception as e:
                    list_logger.error(f"Error occured inside pop Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at pop Method: {e}")



        try:
            def remove(self,elmnt) -> None:
                """Removes the first item with the specified value"""
               try:
                    list_logger.info(f"Using remove method with parameter: element={elmnt}")
                    return self.mylist.remove(elmnt)
                except Exception as e:
                    list_logger.error(f"Error occured inside remove Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at remove Method: {e}")



        try:
            def reverse(self) -> list:
                """Reverses the order of the list"""
                try:
                    list_logger.info(f"Using reverse method")
                    return self.mylist.reverse()
                except Exception as e:
                    list_logger.error(f"Error occured inside reverse Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at reverse Method: {e}")



        try:
            def sort(self,is_reverse=False) -> list:
                """Sorts the list"""
               try:
                    list_logger.info(f"Using sort method with parameter: reverse={is_reverse}")
                    return self.mylist.sort(reverse=is_reverse)
                except Exception as e:
                    list_logger.error(f"Error occured inside sort Method: {e}")
        except Exception as e:
            list_logger.error(f"Error occured at sort Method: {e}")

except Exception as e:
    logger.error(f"List Class Error Occured: {e}")
else:
    logger.info(f"No Error Occured in List CLass")
