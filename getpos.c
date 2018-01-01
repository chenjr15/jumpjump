#include <stdio.h>
#include <windows.h>
#include <conio.h>

int getPos(POINT* p,unsigned delay){
    while(delay--){
		Sleep(1000);
		printf("measure starts at %d seconds \n",delay);
	}
	GetCursorPos(p);
	printf("Located at (%d,%d) \n",p->x,p->y);
	return 0;
}
int main(){
    POINT p;
    FILE * fd;
    getPos(&p,2);
    fd= fopen("point.txt","w");
    fprintf(fd,"%d,%d",p.x,p.y);
    fclose(fd);
}
