#include<stdio.h>

int lookup[] = {158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162};

// The exact same hash function.
char hash(int var0, int var1){
    int var2 = ((var0 ^ var1) + var0 & var0 + var1) % 26;
    return (char)(65 + var2);
}

int main(int argc, char **argv){
    size_t pass_length = (sizeof(lookup)/sizeof(int)) >> 1;
    printf("Size of pass should be: %zu\n", pass_length);

    //Find what is the hash value at each element
    printf("Pass should be: ");
    for(int i = 0; i < pass_length; i++){
        printf("%c", hash(lookup[2 * i], lookup[2 * i + 1]));
    }
    //Obsessive-compulsive disorder
    printf("\n");
}