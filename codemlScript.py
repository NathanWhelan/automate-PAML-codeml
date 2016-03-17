#!/usr/bin/python

#########################################################################################################################
#This script was written by Nathan Whelan.

# THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
# OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE
# SOFTWARE.
##########################################################################################################################

##This script utilizes codeml in PAML by Ziheng Yang. If you use this script please also cite PAML.

##BIOPYTHON IS REQUIRED FOR THIS SCRIPT!


##This script can be used to automate running the codeml PAML package(e.g. if you have hundreds of genes you want to fit to a model).
#A codeml ctl file should be in your working directory with the parameters you wish to use.

from __future__ import division
from Bio.Phylo.PAML import codeml ##Biopython PAML
import sys

#This program takes three inputs: the alignment in phylip format, a treefile in Newick format, and outputfile name
#It returns a nested dictionary with various results depending on analysis
if len(sys.argv) != 4:
        print "Error.  There should be three inputs. An alignment in pyhlip format, a tree file, and the name for the output file"
        quit()

cml = codeml.Codeml()
cml.read_ctl_file("codeml.ctl") ##CTL File. See PAML manual for format.
cml.alignment = sys.argv[1]
cml.tree = sys.argv[2]
cml.out_file = sys.argv[3]

name=sys.argv[1]
print name
name=sys.argv[1]
print name
name2=name[0:5]+"_omega.out"
print name2
results1 = cml.run(verbose=True)
