import os
from typing import Optional

from owlready2 import Ontology, get_ontology


class OntologyManager:

    ontology: Optional[Ontology] = None
    crax_path: str = os.path.join(os.path.curdir, "..", "resources", "crax.owl")

    def __init__(self, crax_path: Optional[str] = None):

        if crax_path:
            self.crax_path = crax_path

        # clear file
        os.remove(self.crax_path) if os.path.exists(self.crax_path) else None
        f = open(self.crax_path, "w")
        self.ontology = get_ontology("file://" + self.crax_path).load()
