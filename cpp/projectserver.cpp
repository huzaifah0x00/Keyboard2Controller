#include <winsock2.h>
#include <ws2tcpip.h>
#include <iostream>

#pragma comment(lib, "Ws2_32.lib")
#define DEFAULT_PORT "27015"

int main() {
	struct sockaddr{
		unsigned short sa_family;
		char sa_data[14];
	}

	struct sockaddr_in{
		short int sin_family;
		unsigned short int sin_port;
		struct in_addr sin_addr;
		unsigned char sin_zero[8];
	}
	WSADATA wsaData;
	int iResult;
	if (ListenSocket == INVALID_SOCKET) {
	    printf("Error at socket(): %ld\n", WSAGetLastError());
	    freeaddrinfo(result);
	    WSACleanup();
	    return 1;
	}
	//Initialize Winsock
	iResult = WSAStartup(MAKEWORD(2,2), &wsaData);
	if (iResult != 0){
		std::cout << "WSTARTUP FAILED" << iResult << "\n";
		return 1;
	}
}

