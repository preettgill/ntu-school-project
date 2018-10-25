//Name: Harpreet Kaur
//Matric Number: U1122042G
//LAB Group: FSP 4

#include <stdio.h>
#include <string.h>
#define MAX_SIZE 80

void convertToPigLatin(char *eword, char *plword);

main()
{
	char eword[MAX_SIZE];
	char plword[MAX_SIZE];
	int cont = 1;
	
	while (cont) {
	printf("English: ");
	scanf("%s", eword);
	
	convertToPigLatin(eword, plword);
	
	printf("Pig Latin: %s\n", plword);
	printf("Continue (1 for yes, 0 for no): ");
	scanf("%d", &cont);
}
return 0;
}

/* add the function code of convertToPigLatin */
void convertToPigLatin(char *eword, char *plword){
	char p[] = "ay";
	int pos = 0,i, ewordLen;

	ewordLen = strlen(eword); // gets length of word
	
	// checks word for vowel
	for (i=0; i<ewordLen; i++) {
		if (eword[i] == 'a' || eword[i] == 'e' || eword[i] == 'i'|| eword[i] == 'o' || eword[i] == 'u' || eword[i] == 'A' || eword[i] == 'E'|| eword[i] == 'I'|| eword[i] == 'O'|| eword[i] == 'U') {
			pos = i; //gets position of vowel
			break;
		}
	}
	// if letter begins with y,Y or is 0
	if (eword[0] == 'y' || eword[0] == 'Y' || pos == 0) {
		strcpy(plword, eword);
		strcat(plword, p);
	}
	//for letter beginning with vowels
	else {
		
		//copy string to plword from position of eword after vowel
		strcpy(plword, eword + pos);
		//printf("%s\n", eword + pos);
		
		//concatenate plword and eword letters that were before the vowel
		strncat(plword, eword, pos);
		//printf("%s, %s,%d\n",plword, eword,pos);
		strcat(plword,p);
	}
}