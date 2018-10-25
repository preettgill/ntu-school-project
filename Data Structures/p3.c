//Name: Harpreet Kaur
//Matric Number: U1122042G
//LAB Group: FSP 4

#include <stdio.h>
#include <stdio.h>

void reverseDigits(int n, int *result);

main(void)
{
	int result;
	int n;
	int cont = 1;

	while (cont) {
		result = 0;
		printf("Enter a number: ");
		scanf("%d", &n);
		reverseDigits(n, &result);

		printf("result = %d\n", result);
		printf("Continue (1 for yes, 0 for no): ");
		scanf("%d", &cont);
	}
	return 0;
}

/* add the function code of reverseDigits */
void reverseDigits(int n, int *result){
	
	
	if (n<10){ // terminating condition
		*result = *result*10 + n%10; //reverse digit mtd
	} 
	else{   // recursive condition
		*result = *result*10 + n%10;
		reverseDigits(n/10, result);
	}
	
}
