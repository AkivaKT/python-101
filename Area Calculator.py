import math

def Rec():
    width = input('Enter width: ')
    height = input('Enter height:' )
    try:
        float(width)
        float(height)
    except:
        print('Something went wrong.')
        return Rec()
    RArea = float(width) * float(height)
    return RArea

def Cir():
    radius = input('Enter radius: ')
    try:
        float(radius)
    except:
        print('Something went wrong.')
        return Cir()
    CArea = (float(radius) ** 2) * math.pi
    return round(CArea, 3)

def Tri():
    base = input('Enter base: ')
    height = input('Enter height:')
    try:
        float(base)
        float(height)
    except:
        print('Something went wrong.')
        return Tri()
    TArea = float(base) * float(height) * 0.5
    return TArea
    
def main():
    letterInput = input('Enter T for triangle, C for circle, R for Rectangle: ')
    if letterInput.upper() == 'R':
        print ('Area of the Rectangle is =', Rec())
    elif letterInput.upper() == 'C':
        print ('Area of the Circle is =', Cir())
    elif letterInput.upper() == 'T':
        print ('Area of the Circle is =', Tri())
    else:
        print ('Not a valid option')
        return main()
    
main()
