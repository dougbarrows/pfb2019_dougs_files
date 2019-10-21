#!/usr/bin/env python3

class DNArecord(object):
	def __init__(self, sequence, gene_name, species):
		self.sequence = sequence
		self.gene_name = gene_name
		self.species = species 
	
	def dna_len(self):
		length = len(self.sequence)
		return(length)
		
	def nt_comp(self): #prints a dictionary with the count for each NT
		self.sequence = self.sequence.upper()
		aComp = self.sequence.count("A")
		tComp = self.sequence.count("T")
		gComp = self.sequence.count("G")
		cComp = self.sequence.count("C")
		nComp = self.sequence.count("N")
		nt_count_dict = {"A":aComp, "T": tComp, "G":gComp, "C":cComp, "N":nComp}
		return(nt_count_dict)

	def gc_content(self):
		dna_nt_comp = self.nt_comp()
		GC = (dna_nt_comp["G"] + dna_nt_comp["C"])/(dna_nt_comp["G"] + dna_nt_comp["C"] + dna_nt_comp["A"] + dna_nt_comp["T"] + dna_nt_comp["N"])
		return(GC)

	def fastarize(self):
		return(self.gene_name +  " | "+ self.species + "\n" + self.sequence)


dna_obj = DNArecord("AGCGCGTC", "test_gene", "Homo Sapiens")

print(dna_obj)
print(dna_obj.sequence)
print(dna_obj.gene_name)
print(dna_obj.species)
print("Length:", dna_obj.dna_len())
print("NT Count:", dna_obj.nt_comp())
print("GC Content:", dna_obj.gc_content())
print(dna_obj.fastarize())

class multiDNArecord(object):
	def __init__ (self, object1, object2):
		self.object1 = object1
		self.object2 = object2

	def build(self):
		object_list = [self.object1, self.object2]
		object_dict = {}
		count = 0
		for obj in object_list:
			temp_dict = {}
			temp_dict["sequence"] = obj.sequence
			temp_dict["gene_name"] = obj.gene_name
			temp_dict["species"] = obj.species
			object_dict[count] = temp_dict
			count+=1
		return(object_dict)

	def compare(self):
		object_dict = self.build()
		if (object_dict[0]["sequence"] == object_dict[1]["sequence"]):
			if (object_dict[0]["gene_name"] == object_dict[1]["gene_name"]):
				if (object_dict[0]["species"] == object_dict[1]["species"]):
					return(True)
		else:
			return(False)

	#def DNArecord_compare(self):
	
dna_obj2 = DNArecord("TGCATTA", "test_gene", "Homo Sapiens")
		
multi_object_same = multiDNArecord(dna_obj, dna_obj)
multi_object_dif = multiDNArecord(dna_obj, dna_obj2)

print(multi_object_same.build())
print(multi_object_same.compare())

print(multi_object_dif.build())
print(multi_object_dif.compare())
