#include <stdio.h> 
#include <stdlib.h> 
#include "schema.h"

void main()   
{  
   TuneFile tune;
   FILE *fptr;

   if ((fptr = fopen("BF02D185C1734932B7D75DADA544CC63","rb")) == NULL)
   {
       printf("Error opening file");
       exit(1);
   }

   fread(&tune.metadata.version, sizeof(tune.metadata.version), 1, fptr); 
   fread(&tune.metadata.ordinal, sizeof(tune.metadata.ordinal), 1, fptr); 
   fread(&tune.metadata.unknown1, sizeof(tune.metadata.unknown1), 1, fptr);

   fread(&tune.upgrades, sizeof(tune.upgrades), 1, fptr);
   fread(&tune.tuning, sizeof(tune.tuning), 1, fptr);
   fclose(fptr); 

   printf("fifth gear: %.15f\n", (tune.tuning.fifth_gear));
}
