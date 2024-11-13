import unittest
import crax
import inspect



def recursive_subclasses(cls):
    """
    :param cls: The class.
    :return: A list of the classes subclasses.
    """
    return cls.__subclasses__() + [g for s in cls.__subclasses__() for g in recursive_subclasses(s)]


class CraxTestCase(unittest.TestCase):

    def test_creation(self):
        for cls in recursive_subclasses(crax.Base):
            cls: crax.Base
            cls.set_comment_to_docstring()
        crax.ontology.save()

if __name__ == '__main__':
    unittest.main()
