import math
import time

def get_digit(digit, data):
    if digit == 0:
        return 0
    
    if digit == 1:
        return data%10

    big = math.floor(data/10**(digit-1))
    small = math.floor(data/10**(digit)) * 10
    res = big - small

    return res

def dec2display(dec):
    converter = {
        '0': "0000001",
        '1': "1001111",
        '2': "0010010",
        '3': "0000110",
        '4': "1001100",
        '5': "0100100",
        '6': "0100000",
        '7': "0001111",
        '8': "0000000",
        '9': "0001100",
        }
    
    if dec > 9:
        #print("ERR: Valor decimal maior do que o esperado")
        return "0111000"
    
    return converter.get(str(dec), "0111000")

def mult_dec2display(val, qtd_num):
    if val > qtd_num-1:
        u_disp = dec2display(10)
        d_disp = dec2display(10)
        h_disp = dec2display(10)
        t_disp = dec2display(10)
        displays =  t_disp + h_disp + d_disp + u_disp
        return displays
    
    # 4 Less significatn digit
    unit = get_digit(1, val)
    decimal = get_digit(2, val)
    hundred = get_digit(3, val)
    thousand = get_digit(4, val)

    # 7 segments display
    u_disp = dec2display(unit)
    d_disp = dec2display(decimal)
    h_disp = dec2display(hundred)
    t_disp = dec2display(thousand)
    
    # 4 x 7segments display
    displays =  t_disp + h_disp + d_disp + u_disp

    return displays

if __name__ == '__main__':
    ts = time.process_time()
    fname = 'bin2display.txt'
    bits = 14
    max_addr = 2**bits-1
    qtd_num = 10000

    print('--Parameters--\n'
          'Path: {0}\n'
          'Bit addres: {1}\n'
          'Max addres quantity: {2}\n'
          'Max display num: {3}'
          .format(fname, bits, max_addr, qtd_num-1))

    fd = open(fname, 'w')
     
    for val in range (max_addr+1):
        # displays
        displays = mult_dec2display(val, qtd_num)
        
        # write file
        fd.write('{0}'.format(displays))
        fd.write('\n')

    fd.close()

    tf = time.process_time()
    dt = tf-ts
    print()
    print('Process time: {0}\n'
          'Closing application...'.format(dt))
    
