package main

import (
	"fmt"
	"net"
	"bufio"
	//"strings"
)

func main() {
	fmt.Println("Launching Server...")

	// listen for connections
	ln,_ := net.Listen("tcp",":8081")
	conn,_ := ln.Accept()

	for {

		message,_ := bufio.NewReader(conn).ReadString('\n')

		fmt.Println("message recieved :", string(message))

		newmessage := "ack"

		conn.Write([]byte(newmessage+"\n"))
	}
}