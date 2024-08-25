# The Interface Segregation Principle (ISP) suggests that clients should not
# be forced to depend on interfaces they do not use. It's better to create
# small, specific interfaces than to have a large, general-purpose interface.

# Example before applying ISP:

class Printer:
    def print_document(self, document):
        pass

    def scan_document(self, document):
        pass

    def fax_document(self, document):
        pass

# This Printer interface is too broad. Not all printers support scanning or faxing.
# For example, a basic printer might only print documents, but it is forced to
# implement scan_document and fax_document methods even if they are irrelevant.

class BasicPrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        # BasicPrinter doesn't need this method, but it has to implement it.
        raise NotImplementedError("BasicPrinter does not support scanning")

    def fax_document(self, document):
        # BasicPrinter doesn't need this method, but it has to implement it.
        raise NotImplementedError("BasicPrinter does not support faxing")

class MultiFunctionPrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")

    def fax_document(self, document):
        print(f"Faxing: {document}")

# The above example violates ISP because BasicPrinter has to implement methods
# for scanning and faxing, even though it doesn't support these features.

# Let's refactor this code to adhere to the Interface Segregation Principle:

# Example demonstrating the Interface Segregation Principle (ISP)
# ISP states that no client should be forced to depend on methods it does not use.

from abc import ABC, abstractmethod

# Define an interface for printing
class Printer(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        pass

# Define an interface for scanning
class Scanner(ABC):
    @abstractmethod
    def scan(self, document: str) -> None:
        pass

# Define an interface for faxing
class Fax(ABC):
    @abstractmethod
    def fax(self, document: str) -> None:
        pass

# A class that only prints, does not need to implement other methods
class BasicPrinter(Printer):
    def print(self, document: str) -> None:
        print(f"Printing: {document}")

# A class that can print, scan, and fax
class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print(self, document: str) -> None:
        print(f"Printing: {document}")

    def scan(self, document: str) -> None:
        print(f"Scanning: {document}")

    def fax(self, document: str) -> None:
        print(f"Faxing: {document}")

# Main function to test the classes
if __name__ == "__main__":
    document = "My Document"

    # BasicPrinter can only print
    basic_printer = BasicPrinter()
    basic_printer.print(document)

    # MultiFunctionPrinter can print, scan, and fax
    mfp = MultiFunctionPrinter()
    mfp.print(document)
    mfp.scan(document)
    mfp.fax(document)
# This refactoring adheres to the Interface Segregation Principle.
# Now, BasicPrinter only implements the methods it needs, and MultiFunctionPrinter
# implements all the methods for printing, scanning, and faxing.

# This approach makes the code more modular and easier to maintain, as each class
# is only concerned with the methods it actually needs.

