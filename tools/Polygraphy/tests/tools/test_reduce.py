import argparse
import sys
import onnx
from polygraphy.tools.debug.subtool.reduce import Reduce



def main():
    parser = argparse.ArgumentParser(description="Test the functionality of Reduce")
    parser.add_argument("model", help="The ONNX model")
    parser.add_argument(
        "--fail-node",
        help="The name(s) of the node(s) that 'fails'. "
        "If multiple nodes are specified, they must all be present to cause a failure.",
        required=True,
        nargs="+",
    )
    parser.add_argument(
        "--default-return-code", help="The return code to use when there are no failures. ", default=0, type=int
    )
    parser.add_argument(
        "--fail-return-code", help="The return code to use when there is a failure. ", default=1, type=int
    )

    args = parser.parse_args()

    print("Running test_reduce.py")
    
    return