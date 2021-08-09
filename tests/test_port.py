
import port_mgmt.ports as pm
def test_for_port():
    port_management = pm.Port()
    # assert port_management.getInstance()==port_management #pass test
    # geo=port_management.get_geodataframe()
    print(port_management.get_geodataframe().shape)
    # assert port_management.get_geodataframe().shape==(49864, 14) #49864 port data and 14 features

def test_for_nearest_port():
    port_management = pm.Port()
    yp=port_management.nearest_port(10.3,-4.2)
    print(yp)
    assert yp.iloc[0].name==9598  

def test_for_env_factors():
    port_management = pm.Port()
    yp=port_management.env_factors(10.3,-4.2)
    print(yp)
    assert yp[0]==28.17 
    assert yp[1]== 22.25
    assert yp[2]== 25.5 
    assert yp[3] ==32.05

def test_for_env_distance():
    port_management = pm.Port()
    ed=port_management.env_distance((10.3,-4.2),(14.3,45.2))
    print(ed)
    assert ed==20.622
    
if __name__ == "__main__":
    test_for_nearest_port()
    test_for_port()
    test_for_env_factors()
    test_for_env_distance()