#include <stdio.h>
#define isdigit(c) ((c) >= '0' && (c) <= '9')              //检测是否是数字
#define CHANGE_LOWER 'A' - 'a'                             //大写转小写
#define MAX_GOSUB_DEPTH 20                                 //gosub 语句最多20次嵌套
#define MAX_STR_LENGTHSTR_LENGTH 50                        //string长度最多50字节
#define MAX_FOR_DEPTHMAX_FOR_DEPTH 6                       //for循环最多嵌套次数5
#define MAX_VARNUM 40                                      //最多储存40个变量
#define MAX_NUMLEN 20                                      //number最大长度
static char const *program_ptr, *ptr, *nextptr, *startptr; //用于词法分析的指针

typedef enum
{
    BINARY,
    OCTAL,
    DECIMAL,
    //Hexadecimal
    HEXADECIMAL,

} NUM_TYPE;

NUM_TYPE state_num = DECIMAL;
static char *binstart, *binnow;

typedef enum
{
    ERR,
    END,
    ID,
    NUM,
    STR,
    R0,
    R1,
    R2,
    R3,
    R4,
    R5,
    R6,
    R7,
    //STATU,CPC,EPC,IE,TVEC0,TVEC1,TVEC2,TVEC3,
    OPERATOR,
    KW_SEC,
    KW_GLB,
    KW_EQU,
    KW_TIMES,
    KW_DB,
    KW_DD,
    KW_DW,
    COMMA,
    SEMICOLON,
    PLUS,
    MINUS,
    AND,
    OR,
    ASTRISK,
    SLASH,
    PERCENT,
    LEFTBRACKET,
    RIGHTBRACKET,
    LIGHTER,
    GREATER,
    EQUAL,
    CR,

} TAG;
typedef enum OPERATOR
{
    KADD,
    KSUB,
    KAND,
    KOR,
    KXOR,
    KSR,
    KSL,
    KSRA,
    KSLT,
    KSLTU,
    KEQ,
    KNEQ,
    KBRA0,
    KJL,
    KAPC,
    KJMP,
    KWCR,
    KRCR,
    KRET,
    KFENCE,
    KLI,
    KLB,
    KSB,
};

typedef struct keyword_token
{
    char *keyword;
    int tag;
} KEYS_OPERATOR;

static TAG tag_now = ERR;

const KEYS_OPERATOR KEYWORDS_OPERATOR[] = {
    {"add", KADD},
    {"sub", KSUB},
    {"and", KAND},
    {"or", KOR},
    {"xor", KXOR},
    {"sr", KSR},
    {"sl", KSL},
    {"sra", KSRA},
    {"slt", KSLT},
    {"sltu", KSLTU},
    {"eq", KEQ},
    {"neq", KNEQ},
    {"bra0", KBRA0},
    {"jl", KJL},
    {"apc", KAPC},
    {"jmp", KJMP},
    {"wcr", KWCR},
    {"rcr", KRCR},
    {"ret", KRET},
    {"fence", KFENCE},
    {"li", KLI},
    {"lb", KLB},
    {"sb", KSB},
};

int atoi(const char *src);
void *memcpy(void *dest, const void *src, int count);
char *strchr(char *str, const char c);
unsigned int strlen(const char *str);
char *strncpy(char *dest, const char *str, int count);
int strncmp(const char *str1, const char *str2, int count);
int strcmp(const char *str1, const char *str2);
char *itoa(int num, char *str, int radix);
char *strcpy(char *strDest, const char *strSrc);
void *memset(void *dst, int val, int count);
void *memset(void *dst, int val, int count)
{
    void *ret = dst;
    while (count--)
    {
        *(char *)dst = (char)val;
        dst = (char *)dst + 1;
    }
    return ret;
}
char *itoa(int num, char *str, int radix)
{
    char index[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //索引表
    unsigned unum;                                         //存放要转换的整数的绝对值,转换的整数可能是负数
    int i = 0, j, k;                                       //i用来指示设置字符串相应位，转换之后i其实就是字符串的长度；转换后顺序是逆序的，有正负的情况，k用来指示调整顺序的开始位置;j用来指示调整顺序时的交换。

    //获取要转换的整数的绝对值
    if (radix == 10 && num < 0) //要转换成十进制数并且是负数
    {
        unum = (unsigned)-num; //将num的绝对值赋给unum
        str[i++] = '-';        //在字符串最前面设置为'-'号，并且索引加1
    }
    else
        unum = (unsigned)num; //若是num为正，直接赋值给unum

    //转换部分，注意转换后是逆序的
    do
    {
        str[i++] = index[unum % (unsigned)radix]; //取unum的最后一位，并设置为str对应位，指示索引加1
        unum /= radix;                            //unum去掉最后一位

    } while (unum); //直至unum为0退出循环

    str[i] = '\0'; //在字符串最后添加'\0'字符，c语言字符串以'\0'结束。

    //将顺序调整过来
    if (str[0] == '-')
        k = 1; //如果是负数，符号不用调整，从符号后面开始调整
    else
        k = 0; //不是负数，全部都要调整

    char temp;                         //临时变量，交换两个值时用到
    for (j = k; j <= (i - 1) / 2; j++) //头尾一一对称交换，i其实就是字符串的长度，索引最大值比长度少1
    {
        temp = str[j];               //头部赋值给临时变量
        str[j] = str[i - 1 + k - j]; //尾部赋值给头部
        str[i - 1 + k - j] = temp;   //将临时变量的值(其实就是之前的头部值)赋给尾部
    }

    return str; //返回转换后的字符串
}

char *strncpy(char *dest, const char *str, int count)
{
    //assert(dest != NULL&&str != NULL);
    char *ret = dest;
    while (count-- && (*dest++ = *str++))
    {
        ;
    }
    if (count > 0) //当上述判断条件不为真时并且count未到零，在dest后继续加/0；
    {
        while (count--)
        {
            *dest++ = '/0';
        }
    }
    return ret;
}

int strcmp(const char *str1, const char *str2)
{
    int ret = 0;
    while (!(ret = *(unsigned char *)str1 - *(unsigned char *)str2) && *str1)
    {
        str1++;
        str2++;
    }
    if (ret < 0)
    {
        return -1;
    }
    else if (ret > 0)
    {
        return 1;
    }
    return 0;
}

char *strcpy(char *strDest, const char *strSrc)
{
    char *p = NULL;
    if (strDest == NULL || strSrc == NULL)
    {
        return NULL;
    }
    p = strDest;
    while ((*strDest++ = *strSrc++) != '\0')
    {
        //MY_PRINT("ch\n");
    };
    return p;
}

int strncmp(const char *str1, const char *str2, int count)
{

    if (!count)
        return 0;
    while (--count && *str1 && *str1 == *str2)
    {
        str1++;
        str2++;
    }
    return (*str1 - *str2);
}

void *memcpy(void *dest, const void *src, int count)
{
    if (dest == NULL || src == NULL)
    {
        return NULL;
    }
    char *pdest = (char *)dest;
    char *psrc = (char *)src;
    while (count--)
    {
        *pdest++ = *psrc++;
    }
    return dest;
}

char *strchr(char *str, const char c)
{

    while (*str != '\0' && *str != c)
    {
        str++;
    }

    return (*str == c ? str : NULL);
}

unsigned int strlen(const char *str)
{

    unsigned length = 0;
    while (*str != '\0')
    {
        length++;
        str++;
    }
    return length;
}

char *strtrim(char *s)
{
    char *p = s;
    char *q = s;
    char *end = s;
    while (*p == ' ' || *p == '\t')
        ++p;
    while (*q = *p)
    {
        if (*q != ' ' && *q != '\t')
            end = q + 1;
        ++q, ++p;
    }
    *end = '\0';

    return s;
}

////////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////

double atof(const char *str)
{
    const char *p = str;
    int sign = 1;
    while (*p == ' ')
        ++p;       //忽略前置空格
    if (*p == '-') //考虑是否有符号位
    {
        sign = -1;
        ++p;
    }
    else if (*p == '+')
        ++p;
    int hasDot = 0, hasE = 0;
    double integerPart = 0.0, decimalPart = 0.0;
    //遇到'e'或'.'字符则退出循环,设置hasE和hasDot。
    for (; *p; ++p)
    {
        if (isdigit(*p)) //若p指向的字符为数字则计算当前整数部分的值
            integerPart = 10 * integerPart + *p - '0';
        else if (*p == '.')
        {
            hasDot = 1;
            p++;
            break;
        }
        else if (*p == 'e' || *p == 'E')
        {
            hasE = 1;
            p++;
            break;
        }
        else //如果遇到非法字符,则截取合法字符得到的数值,返回结果。
            return integerPart;
    }

    //上一部分循环中断有三种情况,一是遍历完成,这种情况下一部分的循环会自动跳过；其次便是是遇到'.'或'e',两种hasE和hasDot只可能一个为真,若hasDot为真则计算小数部分,若hasE为真则计算指数部分。
    int decimalDigits = 1;
    int exponential = 0;
    for (; *p; p++)
    {
        if (hasDot && isdigit(*p))
            decimalPart += (*p - '0') / pow(10, decimalDigits++);
        else if (hasDot && (*p == 'e' || *p == 'E'))
        {
            integerPart += decimalPart;
            decimalPart = 0.0;
            hasE = 1;
            ++p;
            break;
        }
        else if (hasE && isdigit(*p))
            exponential = 10 * exponential + *p - '0';
        else
            break;
    }
    //上一部分较难理解的就是else if (hasDot && (*p == 'e' || *p == 'E')) 这一特殊情况,对于合法的浮点数,出现'.'字符后,仍然有可能是科学计数法表示,但是出现'e'之后,指数部分不能为小数(这符合<string.h>对atof()的定义)。这种情况变量IntegerPart和decimalPart都是科学计数法的基数,因此有integerPart += decimalPart(这使得IntergerPart的命名可能欠妥,BasePart可能是一种好的选择)。
    //上一部分循环结束一般情况下就能返回结果了,除非遇到前文所述的特殊情况，对于特殊情况需要继续计算指数。
    if (hasE && hasDot)
        for (; *p; p++)
            if (isdigit(*p))
                exponential = 10 * exponential + *p - '0';
    return sign * (integerPart * pow(10, exponential) + decimalPart);
}

int atoi(const char *src)
{
    //assert(NULL != src);
    int _num = 0;
    int _sign = 0;
    while ('0' == *src || ' ' == *src || '\n' == *src || '-' == *src || '+' == *src) //如果有空,空格或者换行跳过去
    {
        if (*src == '-')
            _sign = 1;

        src++;
    }

    while (*src >= '0' && *src <= '9')
    {
        _num = _num * 10 + *src - '0';
        src++;
    }

    if (_sign == 1)
        return -_num;
    else
        return _num;
}

/*
param:no
return:enum of char

*/
static int if_one_char(void)
{
    switch (*ptr)
    {
    case '\n':
        return CR;

    case ',':
        return COMMA;

    case ';':
        return SEMICOLON;

    case '+':
        return PLUS;

    case '-':
        return MINUS;

    case '&':
        return AND;

    case '|':
        return OR;

    case '/':
        return SLASH;

    case '*':
        return ASTRISK;

    case '(':
        return LEFTBRACKET;

    case ')':
        return RIGHTBRACKET;

    case '<':
        return LIGHTER;

    case '>':
        return GREATER;

    case '=':
        return EQUAL;

    default:
        return 0;
    }
}

int get_number()
{
    int i;
    int findsatate;
    state_num = DECIMAL;
    if (*ptr == 0)
    {
        findsatate = 1;
    }
    for (i = 0; i < MAX_NUMLEN; ++i)
    {
        if (i == 1 && findsatate)
        {
            switch (ptr[i])
            {
            case 'x':
                state_num == HEXADECIMAL;
                break;
            case 'X':
                state_num == HEXADECIMAL;
                break;
            case 'b':
                state_num == BINARY;
                break;
            case 'B':
                state_num == BINARY;
                break;
            default:
                state_num == OCTAL;
                break;
            }

            else
            {
                if (!isdigit(ptr[i]) && i > 0)
                {
                    nextptr = ptr + i;
                    return NUM;
                }
            }
        }
    }
}

static TAG get_next_tag(void)
{
    KEYS_OPERATOR const *kt;
    int i;
    if (*ptr == 0)
    {
        return END;
    }
    if (isdigit(*ptr)) //数字
    {

        get_number();
    }
}

void search_init(const char *porgram)
{
    ptr = program;
}

TAG search_tag()
{
    return tag_now;
}

int search_finish()
{
    return *ptr == 0 || tag_now == END;
}

void search_next(void) //寻找下一个tag
{
    if (search_finish()) //寻找结束
    {
        return;
    }
    prt = nextptr; //临时指针赋值
    while (*ptr == ' ')
    {
        ++ptr;
    }
    tag_now = get_next_tag(); //寻找下一个tag
    return;
}

int main()
{
    int line = 10;
    unsigned char binarray[line * 2];
    binarray[0] = 12;
    binnow = binarray;
    binnow++;
    *binnow = 255;
    *printf("%d", *binnow);
}
