#!/usr/bin/perl 

use CGI::Carp qw(fatalsToBrowser);
use CGI qw(:standard);

print header(); 

my $q = new CGI; 
print $q->header(); 

my $response = $q->param('g-recaptcha-response');



use lib qw(./lib);

use Google::reCAPTCHA::v3; 

use Data::Dumper; 

my $rec = Google::reCAPTCHA::v3->new({
	-secret => '',
}); 
my $r = 

	$rec->request(
		{ 
			-response => $response, 
		}
	);
	
	print '<pre>';
	print "\n";
	print Dumper($r); 
	print "\n";
	#print $r->{success};
#	print "\n";
	 
print "ok.\n";