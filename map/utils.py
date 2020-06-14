import folium

def generate_beacon_map():
    kenya = folium.Map(
        location=[-1.28333, 36.81667],
        zoom_start=12,
        # width=400,
        # height=300,
        control_scale=True,
    )

    # RSK Radio Shack 5Z4RS
    folium.Marker(
        location=[-1.303640, 36.785963],
        zoom_start=12,
        popup="RSK Radio Shack 5Z4RS",
        tooltip="5Z4RS Radio Shack",
    ).add_to(kenya)

    # NCDXF beacon 5Z4B & 2m Repeater
    folium.Marker(
        location=[-1.296058, 36.761117],
        zoom_start=12,
        popup="NCDXF beacon 5Z4B & 2m Repeater",
        tooltip="NCDXF Beacon 5Z4B",
    ).add_to(kenya)

    # Communications Authority of Kenya
    folium.Marker(
        location=[-1.262335, 36.757378],
        zoom_start=12,
        popup="Communications Authority of Kenya",
        tooltip="CA Kenya",
    ).add_to(kenya)

    # Planning House, Lower Kabete
    folium.Marker(
        location=[-1.245479, 36.771003],
        zoom_start=12,
        popup="Planning House, Lower Kabete",
        tooltip="Planning Hse",
    ).add_to(kenya)

    return kenya._repr_html_()
