"""Wox Plugin class for unit conversions"""
import pkgutil
from wox import Wox
if pkgutil.find_loader("pint"): #Check for pint
    import pint
    ureg = pint.UnitRegistry()
    ureg.default_format = ".5nP"
    dependecies_exist = True
else:
    dependecies_exist = False


class UnitConversion(Wox):
    """Converts units, interfaces with Wox"""

    def query(self, query):
        """Returns instructions for the user or the results of the user's search string"""
        result = []
        if dependecies_exist == False:
            result.append({
                "Title": "Unit Converter",
                "SubTitle": "This plugin requieres the python module 'pint'. Run 'pip install pint' to install pint.",
                "IcoPath": "Images\\app.png"
            })
        elif " to " in query:
            src, target = query.split(" to ")
            try:
                value = ureg.Quantity(src)
                answer = value.to(target)
            except Exception as e:
                answer = f"Something failed. {e}"
            result.append({
                "Title": f"{target}",
                "SubTitle": f"{answer}",
                "IcoPath": "Images\\app.png"
            })
        else:
            result.append({
                "Title": "Unit Converter",
                "SubTitle": "Please enter a query in the format (number) (sourceUnit) to (targetUnit)",
                "IcoPath": "Images\\app.png"
            })
        return result

if __name__ == "__main__":
    UnitConversion()