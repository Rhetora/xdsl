import pytest

from xdsl.dialects.test import TestOp
from xdsl.ir import Block, Region


def test_add_attached_region():
    op1 = TestOp()
    op2 = TestOp()
    region = Region(Block())

    # Attach region to op1
    op1.add_region(region)

    with pytest.raises(
        ValueError,
        match="Cannot add region that is already attached on an operation",
    ):
        # Try to attach the same region to op2
        op2.add_region(region)
