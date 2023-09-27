from django import forms
# from fractions import Fraction
import numpy as np 

# functions
def is_linearly_independent(base):
    matrix=np.array(base)
    rank=np.linalg.matrix_rank(matrix)
    if rank==len(base):
        return True 
    else:
        return False
    
def get_float_base(matrix_str):
    rows = matrix_str.strip().split('\n') 
    float_base = []
    for row in rows:
        elements = row.split()
        processed_row = []
        for i in range(len(elements)):                         # handles input with √() and /
            elements[i]=elements[i].replace('√', 'np.sqrt')
            processed_row.append(float(eval(elements[i])))
        float_base.append(processed_row)
    return float_base

def processInner(input):
    dict={'X₁':'x1', 'X₂':'x2', 'X₃':'x3', 'X₄':'x4', 'Y₁':'y1', 'Y₂':'y2', 'Y₃':'y3', 'Y₄':'y4', '+':'+', '\u2212':'-', '·':'*', '^':'**'}
    processed_str= input
    for key,value in dict.items():
        processed_str= processed_str.replace(key,value)
    return processed_str

class HomeForm(forms.Form):
    error_css_class='error'

    innerChoice=forms.BooleanField(label='Use standard inner product' ,
                                   initial=True, 
                                   required=False,
                                   widget=forms.CheckboxInput({'id':'innerChoice', 
                                                               'style':'cursor: pointer;'}))
    
    newInner=forms.CharField( max_length=50, 
                              label='Or enter new inner product',
                              required=False, 
                              widget=forms.TextInput(attrs={'id':'newInner', 
                                                            'placeholder': '(Optional)', 
                                                            'readonly': True}))
    
    base = forms.CharField( max_length=100,
                            label='Enter your base',
                            widget=forms.Textarea(attrs={'id':'base-input', 'inputmode': 'decimal',
                                                          'rows': 5, 
                                                          'cols': 20, 
                                                          'placeholder': ' -2   2   √(-3)/2\n -1   1   √(3/2)\n  2   0   1/√(3)'}))

    def clean_newInner(self):
        newInner=self.cleaned_data.get("newInner")
        newInner=processInner(newInner)
        return newInner
    
    def clean_base(self):
        matrix_str=self.cleaned_data.get("base")      
        try:
            t_matrix=get_float_base(matrix_str)   # user input should be numbers
        except:
            raise forms.ValidationError('Invalid base!')
        base = [[row[i] for row in t_matrix] for i in range(len(t_matrix[0]))]
        if not is_linearly_independent(base):
            raise forms.ValidationError('Base is not linearly independent!')
        return base

#   ------------  end of HomeForm -----------------------------------------------------------------------------------------






