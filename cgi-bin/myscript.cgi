#!/usr/bin/perl
read(STDIN,$temp,$ENV{'CONTENT_LENGTH'});
@pairs=split(/&/,$temp);
foreach $item(@pairs)
{
	($key,$content)=split(/=/,$item,2);
	$content=~tr/+/ /;
	$content=~s/%(..)/pack("c",hex($1))/ge;
	$fields{$key}=$content;
}                                       
print "Content-type: text/html\n\n"; 
print "<HTML><BODY>\n";
print "<CENTER>\n";
print "THANK YOU<BR>\n";
print "$fields{fname} $fields{lname}</BR>";
print "I will write<BR>\n";
print "you at<BR>\n";
print "$fields{email}<BR>\n";
print "</CENTER>\n";
print "</BODY></HTML>";

chown www-data 755 /var/www/cgi-bin
chmod 755 /var/www/cgi-bin

open (NEWOUT,">/var/www/cgi-bin/sessions/$SID") || die "can't open the sessions file";
	print NEWOUT "hello\n";
close (NEWOUT) || die "can't close the spaceout file";
