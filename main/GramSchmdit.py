from math import sqrt
from fractions import Fraction


# Define global variables
size_of_vectors=None 
num_of_vectors=None
new_inner= None
inner_choice=None
orth_base=[]
dict = {}
max_range=13


def standard_inner_product(vec1,vec2):
    res=0
    for i in range(size_of_vectors):
        res+=vec1[i]*vec2[i]
    return res      


def non_standard_inner_product(vec1,vec2):
    for i in range(1,size_of_vectors+1):   # creating variables named x1,x2,...y1..
        var_name=f'x{i}'
        var_name2=f'y{i}'
        globals()[var_name]=vec1[i-1]
        globals()[var_name2]=vec2[i-1]
    res= eval(new_inner)  # using the global variable new_inner
    return res


def normalize_vector(vector):
    res=sqrt(inner_choice(vector,vector))
    for i in range(size_of_vectors):
        vector[i] /= res


def multiply(num, list):
    multiplied_list = [item * num for item in list]
    return multiplied_list


def gramSchmid(base):
    for i in range(num_of_vectors):
        sum=[0]*size_of_vectors
        for j in range(i):
            sum= [x+y for x,y in zip(sum,  multiply(inner_choice(base[i],orth_base[j]),orth_base[j])  )]
        e=[x-y for x,y in zip(base[i] , sum)]
        normalize_vector(e)
        orth_base.append(e)


def pretty_base(base):
    create_dict()
    for i, row in enumerate(base):
        for j, element in enumerate(row):
            if isinstance(element, float):
                # Check if element is in the dictionary
                element=round(element,10)
                if element in dict:
                    base[i][j]=dict[element]  # Print the value associated with the element
                elif -element in dict:
                    base[i][j]=f"-{dict[-element]}"
                else:
                    fraction = Fraction(element).limit_denominator()
                    if fraction.denominator == 1:
                        base[i][j] = fraction.numerator  # Convert to integer if denominator is 1
                    else:
                        base[i][j] = f"{fraction.numerator}/{fraction.denominator}"
                

def create_dict():                                  #key=float  value=string
    global dict
    # creating the dict for simplified results
    for i in range(0,max_range):
        value=i
        key=i
        dict[key]=value
    for i in range(1,max_range):
        squared_value=f"√{i}"
        squared_key=sqrt(i)
        if squared_key not in dict:
            dict[squared_key]=squared_value
    # Loop through values of i and j from 1 to 10
    for i in range(1, max_range):
        for j in range(1, max_range):
            # Create the value in the form of "i/j" and add it to the dictionary
            value_normal = f"{i}/{j}"
            key_normal = round(i / j, 10)
            if key_normal not in dict:
                dict[key_normal] = value_normal

            # Create the value in the form of "i/√j" and add it to the dictionary
            if j not in (4,9):
                value_i_over_sqrt_j = f"{i}/√{j}"
                key_i_over_sqrt_j = round(i / sqrt(j), 10)
                if key_i_over_sqrt_j not in dict:
                    dict[key_i_over_sqrt_j] = value_i_over_sqrt_j

            # Create the value in the form of "√i/j" and add it to the dictionary
            if i not in (1,4,9):
                value_sqrt_i_over_j = f"√{i}/{j}"
                key_sqrt_i_over_j = round(sqrt(i) / j, 10)
                if key_sqrt_i_over_j not in dict:
                    dict[key_sqrt_i_over_j] = value_sqrt_i_over_j

            # Create the value in the form of "√i/√j" and add it to the dictionary
            value_sqrt_i_over_sqrt_j = f"√{i}/√{j}"
            key_sqrt_i_over_sqrt_j = round(sqrt(i) / sqrt(j), 10)
            if key_sqrt_i_over_sqrt_j not in dict:
                dict[key_sqrt_i_over_sqrt_j] = value_sqrt_i_over_sqrt_j


# start the proccess 
def main(Xsize_of_vectors,Xnum_of_vectors,Xnew_inner,Xinner_choice,Xbase):
    global size_of_vectors 
    global num_of_vectors
    global new_inner
    global inner_choice
    global base
    global orth_base

    orth_base=[]  #reset it
    size_of_vectors= Xsize_of_vectors
    num_of_vectors=Xnum_of_vectors
    if Xinner_choice:
        inner_choice=standard_inner_product
    else:
        inner_choice=non_standard_inner_product
        new_inner= Xnew_inner
        new_inner=new_inner.lower()
        new_inner=new_inner.replace('^', '**')
        new_inner=new_inner.replace('√', 'sqrt')
    base=Xbase

    
    gramSchmid(base)
    pretty_base(orth_base)
    return orth_base
    
