// C 프로그램 기본 구조
/**********************************************
   파일명: hello.c
   설 명: C프로그램 기본 구조 이해
   작 성: 2025.12 06.

***********************************************/
#include <stdio.h>

/* ----------------------------------------------------
   FNAME: main
   FDESC: entry point
   PARAM: void
   RETURN: int exit code
-------------------------------------------------------*/

int main(void)
{
	// 변수 선언 -------------------------
	// 문법 : 자료형  변수명;
	//		  자료형  변수명 = 초기화;
	int			age = 0;
	short		n1 = 100;
	long long   n2 = 5;
	float		f1 = 3.4;
	double		f2 = 3.4;

	// 표준출력 printf --------------------
	printf("short	 : %d,   %zdbyte\n", n1,  sizeof(n1));
	printf("int		 : %d,   %zdbyte\n", age, sizeof(age));
	printf("longlon  : %lld, %zdbyte\n", n2,  sizeof(n2));  //longlong이라는 의미로 lld를 쓰는거임
	printf("float    : %f,   %zdbyte\n", f1,  sizeof(f1));
	printf("double   : %f,   %zdbyte\n", f2,  sizeof(f2));

	printf("정수 : %d\n", 100);
	printf("실수 : %f\n", 8.9);
	printf("문자 : %c\n", 'A');
	printf("문자열 : %s\n", "A");

	printf("Hello C!");

	return 0;
}