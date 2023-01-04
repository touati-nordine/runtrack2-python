def fruitslegumes(type, saison):

  if type == "fruits" and saison == "hiver":
      print("orange, mandarine, kiwi")

  elif type == "fruits" and saison == "ete":
      print("Poire, fraise, cassis")

  elif type == "legume" and saison == "hiver":
      print("carotte, topinambour, endive")

  elif type == "legume" and saison == "ete":
      print("artichaut, aubergine, navet")

fruitslegumes("fruits", "hiver")
fruitslegumes("fruits", "ete")
fruitslegumes("legume", "hiver")
fruitslegumes("legume", "ete")
