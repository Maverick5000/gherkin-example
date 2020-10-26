from behave import given, when, then
from calculator.simple import SimpleCalculator 

@given(u'Iniciamos la calculadora')
def step_impl(context):
    print(u'STEP: Given Iniciamos la calculadora')
    pass
@when(u'Le paso "{inp}" a la calculadora')
def step_impl(context, inp):
    print(u'STEP: Cuando paso "{}" a la calculadora'.format(inp))
    c = SimpleCalculator()
    c.run(inp)
    context.result = c.lcd
@then(u'Obtengo el resultado "{out}"')
def step_impl(context, out):
    print(u'STEP: Obtengo el resultado "{}"'.format(out))
    assert context.result == int(out), 'Expected {}, got {}'.format(out, context.result)