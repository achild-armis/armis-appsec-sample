#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(param);

print "Content-Type: text/plain\n\n";

my $host = param('host') || 'localhost';

# Vulnerable: unsafely concatenates user input into a shell command
my $output = `ping -c 1 $host 2>&1`;

print $output;
