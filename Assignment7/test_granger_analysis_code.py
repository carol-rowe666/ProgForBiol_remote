from granger_analysis_code import get_gc_content, get_size_class
import nose

#def test_get_gc_content(seq):
#    assert get_gc_content('ggG') == 100

    
def test_get_gc_content():
    assert get_gc_content('GGGGG') == 100
    assert get_gc_content('gggGGG') == 100
    assert get_gc_content('AaTtCcGg') == 50
    #Almost_equal since the actual value has many decimal places. The 2 at the end is to designate to 2 decimal places.
    #Also note that this function will take a string of any letters.
    nose.tools.assert_almost_equal(get_gc_content('AlloftheselettersdonotbelonG'), 3.57, 2)
    assert get_gc_content('aAtg\ngg') == 50
def test_get_size_class():
    assert get_size_class(12.0) == 'large'
    assert get_size_class(10.0) == 'large'
    assert get_size_class(2) == 'small'
    assert get_size_class (999.99) == 'extralarge'
    nose.tools.assert_raises(ValueError, get_size_class, 'beer')
    assert get_size_class (0.004) == 'small'
    assert get_size_class (-0.88) == 'Check earlength value: Zero or negative number likely.'
    