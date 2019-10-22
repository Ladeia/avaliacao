# 
# O sistema hoje possui uma classe para se conectar ao banco de dados local
# Foi feito o deploy do sistema para a aws, mas a string de conexão mudou
# Vocês tem que prover uma nova classe de conexão com o banco e utilizar 
# algum padrão de projeto para flexibilizar as conexões com o banco
# o ideal é que a classe principal não saiba em qual banco ele está conectando
# e que so haja uma instancia de cada classe de conexão ao banco

from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class Builder(ABC):
	"""
	The Builder interface specifies methods for creating the different parts of
	the Product objects.
	"""
	
	@abstractproperty
	def banco(self) -> None:
		pass

	@abstractmethod
	def connection_a(self) -> None:
		pass

	@abstractmethod
	def connection_b(self) -> None:
		pass

class ConcretBuilder1(Builder):

	def __init__(self) -> None:
		self.reset()

	def reset(self) -> None:
		self._banco = Banco()

	@property
	def banco(self) -> Banco:
		banco = self._banco
		self.reset()
		return banco

	def connection_a(self) -> None:
		self._banco.addConnection("1127854", "Batata", "123456", "FDK")

	def connection_b(self) -> None:
		self._banco.addConnection("localhost", "LifusD", "654321", "dev")
		

# classe de conexao com o banco em desenv no mysql
class Banco:

	__instance = None

	def instance(self):
		if not Banco.__instance:
			Banco.__instance = Banco()
		return Banco.__instance

	def __init__(self) -> None:
		self.endereco = "localhost"
		self.usuario = "root"
		self.senha = "senhaforte"
		self.db = "desenv"

	def addConnection(self, endereco, usuario, senha, db) -> None:
		self.endereco = endereco
		self.usuario = usuario
		self.senha = senha
		self.db = db

	def get_url_connection(self):
		return "Server="+self.endereco+";Database="+self.db+";Uid="+self.usuario+";Pwd="+self.senha+";"

class Director:

	def __init__(self) -> None:
		self._builder = None

	@property
	def builder(self) -> Builder:
		return self._builder

	@builder.setter
	def builder(self, builder: Builder) -> None:
		self._builder = builder

	def build_minimal_viable_connection(self) -> None:
		self.builder.connection_a()

	def build_full_featured_connection(self) -> None:
		self.builder.connection_a()
		self.builder.connection_b()




if __name__ == '__main__':
	director = Director()
	builder = ConcretBuilder1()
	director.builder = builder

	director.build_minimal_viable_connection()
	builder.banco.get_url_connection()

	print("\n")

	director.build_full_featured_connection()
	builder.banco.get_url_connection()

	print("\n")

	# Remember, the Builder pattern can be used without a Director class.
	print("Custom product: ")
	builder.connection_a()
	builder.connection_b()
	print(builder.banco.get_url_connection())
