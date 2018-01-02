"""Wox Plugin class for unit conversions"""

import pint
from wox import Wox

class UnitConversion(Wox):
    """Converts units, interfaces with Wox"""

    def query(self, query):
        """Returns the results of the user's search string"""
        src, target = query.split(" to ")
        try:
            value = pint.UnitRegistry().Quantity(src)
            answer = value.to(target)
        except Exception as e:
            answer = f"Something failed. {e}"
        result = [{
            "Title": f"{target.title()}",
            "SubTitle": f"{answer}".title(),
            "IcoPath": "Images\\app.png",
        }]
        return result

if __name__ == "__main__":
    UnitConversion()
