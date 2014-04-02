/*************************************************************************/
/**                                                                     **/
/**     hello_s.c-- simple "hello, world", to demonstrate basic CGI     **/
/**         output.                                                     **/
/**                                                                     **/
/*************************************************************************/

#include <stdio.h>

void main() {

    /** Print the CGI response header, required for all HTML output. **/
    /** Note the extra \n, to send the blank line.                   **/
    printf("Content-type: text/html\n\n") ;
    
    /** Print the HTML response page to STDOUT. **/
    printf("<html>\n") ;
    printf("<head><title>CGI Output</title></head>\n") ;
    printf("<body>\n") ;
    printf("<h1>Hello, world.</h1>\n") ;
    printf("</body>\n") ;
    printf("</html>\n") ;

    exit(0) ;
}
