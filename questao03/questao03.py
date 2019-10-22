# A empresa tinha um software para calcular a folha de ponto de TI
# A aplicação ficou tão boa que o diretor solicitou a mudança para que a mesma aplicação
# funcione para os varios setores e filiais da empresa
# Aplique o padrão composite visando calcular a folha de ponto da empresa

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
	@property
	def nome(self):
		return self._nome

	@property
	def salario(self):
		return self._salario

	@property
	def setor(self):
		return self._setor

	@nome.setter
	def nome(self, nome):
		self._nome = nome
	
	@salario.setter
	def salario(self, salario):
		self._salario = salario

	@setor.setter
	def setor(self, setor):
		self._setor = setor

	def add(self, component):
		pass

	def remove(self, component):
		pass

	def is_composite(self):
		return False

	@abstractmethod
	def operation(self):
		pass

class Funcionario(Component):
	def __init__(self, nome, salario):
		self._nome = nome
		self._salario = salario
		self._setor = ""

	def operation(self):
		return self._salario

class Setor(Component):

	def __init__(self, nome):
		self._funcionarios: List[Component] = []
		self._nome = nome

	def add(self, component):
		self._funcionarios.append(component)
		component._setor = self._nome

	def operation(self):
		custo = 0.0
		for funcionario in self._funcionarios:
			custo += funcionario.operation()
		return custo

class Principal:
	def folha_empresa(self, component):
		print(f"Total: {component.operation()}", end="")

if __name__ == '__main__':
	principal = Principal()

	empresa = Setor("Empresa")

	desenvolvimento = Setor("Desenvolvimento")
	desenvolvimento.add(Funcionario("Batata", 10000))
	desenvolvimento.add(Funcionario("LifusD", 10000))
	
	engenharia = Setor("Engenharia")
	engenharia.add(Funcionario("Fernando", 15000))
	engenharia.add(Funcionario("Gabriel", 15000))
	
	design = Setor("Design")
	design.add(Funcionario("ReyalS", 12000))
	design.add(Funcionario("Taiga", 12000))

	empresa.add(desenvolvimento)
	empresa.add(engenharia)
	empresa.add(design)

	principal.folha_empresa(empresa)

