#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use strict;

# the #-sign is a comment in Perl

# declare the colors hash:
my %colors = (  red => "#ff0000", green=> "#00ff00",
    blue => "#0000ff", black => "#000000",
    white => "#ffffff" );

# print the html headers
print header;
print start_html("Colors");

foreach my $key (keys %colors) {
   print qq(<font color="$colors{$key}">$key</font>\n);   
}

print end_html;



