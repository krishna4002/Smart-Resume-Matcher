from neo4j import GraphDatabase

def recommend_career_paths(skill):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "krishna@2004"))
    query = f"""
    MATCH (s:Skill)-[:LEADS_TO]->(r:Role)
    WHERE s.name = '{skill}'
    RETURN r.name AS role
    LIMIT 5
    """
    with driver.session() as session:
        result = session.run(query)
        return [record["role"] for record in result]