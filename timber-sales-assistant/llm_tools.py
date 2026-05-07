
def get_all_tools():
    available_timber_tool = {
        "name": "get_available_timber_types",
        "description": "Get the list of available timber types and their unit prices in RWF",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": [],
            "additionalProperties": False
        }
    }

    price_tool = {
        "name": "get_timber_price",
        "description": "Get the unit price of a specific timber type in RWF",
        "parameters": {
            "type": "object",
            "properties": {
                "timber_type": {
                    "type": "string",
                    "description": "The type of timber, for example Teak, Pine, or Cedar"
                }
            },
            "required": ["timber_type"],
            "additionalProperties": False
        }
    }


    cost_tool = {
        "name": "calculate_timber_cost",
        "description": "Calculate the total price for a quantity of a specific timber type in RWF",
        "parameters": {
            "type": "object",
            "properties": {
                "timber_type": {
                    "type": "string",
                    "description": "The type of timber, for example Teak, Pine, or Cedar"
                },
                "quantity": {
                    "type": "integer",
                    "description": "The number of timber units the customer wants to buy"
                }
            },
            "required": ["timber_type", "quantity"],
            "additionalProperties": False
        }
    }


    return [
            {"type": "function", "function": available_timber_tool},
            {"type": "function", "function": price_tool},
            {"type": "function", "function": cost_tool}
        ]


