# 基于属性的测试技术（ Property-based testing），是指编写对你的代码来说为真的逻辑语句（即“属性”），
# 然后使用自动化工具来生成测试输入（一般来说，是指某种特定类型的随机生成输入数据），
# 并观察程序接受该输入时属性是否保持不变。如果某个输入违反了某一条属性，则用户证明程序存在一处错误，
# 并找到一个能够演示该错误的便捷示例。

# Hypothesis提供了各种方法。本质上，这些方法对应于内置类型或其他结构，
# 并生成与给定类型匹配的随机数据


def increment(number: int) -> int:
    return number + 1


def decrement(number: int) -> int:
    return number - 1


from hypothesis import given
import hypothesis.strategies as st

@given(st.integers())
def test_increment(x)
    expected = x + 1
    actual = increment(x)
    assert actual == expected
    
    
def div(dividend: int, divisor: int) -> int:
    return dividend // divisor

from hypothesis import example

@given(dividend=st.integers(), divisor=st.integers())
@example(1, 0)
def test_div(dividend, divisor):
    if divisor == 0:
        expected = -1
    else:
        expected = dividend // divisor
    actual = div(dividend, divisor)
    assert actual == expected