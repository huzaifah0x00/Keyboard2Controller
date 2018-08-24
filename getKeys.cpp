#include <Windows.h>
#include <iostream>
#include <typeinfo>
#include "virtualKeyCodes.h"
using namespace std;

int main()
{
	int virtualCodes[] = {VK_UP, VK_DOWN, VK_LEFT,VK_RIGHT,
	A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z,
	VK_1,VK_2,VK_3,VK_4,VK_5,VK_6,VK_7,VK_8,VK_9,
	VK_LCONTROL,VK_LSHIFT,VK_RSHIFT,VK_RCONTROL,
	VK_CAPITAL,
	VK_F4
	};


	#define NUM(virtualCodes) (sizeof(virtualCodes) / sizeof(*virtualCodes))

	cout << NUM(virtualCodes);
	cout << typeid(VK_UP).name();
	for( ; ; )
	{ 
		int i =0 ; for (i=0; i <NUM(virtualCodes); i++)
		{
 			if(GetAsyncKeyState(virtualCodes[i]))
 			{
 				cout << "Key Pressed: " << virtualCodes[i] <<  "" << endl;
 			} 		// cout << "bla" << endl; 	} }
		}
	}
}