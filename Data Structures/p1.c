//Name: Harpreet Kaur
//Matric Number: U1122042G
//LAB Group: FSP 4


#include <stdio.h>

void rowColMin(int A[][5]);

main()
{
	int A[5][5];
	int i, j;
	printf("Enter a 5x5 matrix: \n");
	for (i=0; i<5; i++)
		for (j=0; j<5; j++)
		scanf("%d", &A[i][j]);
		rowColMin(A);
	return 0;
}

/* add the function code of rowColMin() */
void rowColMin(int A[][5]){

int min,i,j,r=0,c=0;
printf("Results:\n");

	//5x5 row
	for (i = 0; i < 5; i++){
		// sets min value 
		min = A[i][0];
		//5x5 col
		for (j = 0; j < 5; j++){
			// checks each row for min value
			if (A[i][j] < min){
				min = A[i][j];
				r = i;
				c = j;
			}
			//checks each col for min value
			if(A[j][i] < min){
				min = A[j][i];
				r = j;
				c = i;
			}
		}

	printf("A[%d], [%d] = %d\n",r,c,min); 
	}

}
