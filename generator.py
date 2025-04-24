import os

# Idiomas y carpetas base
idiomas = {
    "es": "facturas",
    "en": "invoices",
    "fr": "factures"
}

# Traducción de las páginas comunes para cada idioma
paginas_traducidas = {
    "es": ["listar", "crear", "editar", "ver", "eliminar", "enviar", "pdf", "recurrente", "estado", "pagos", "informes", "exportar", "permisos", "nota de crédito", "plantillas", "multi-moneda", "impuestos", "campos personalizados"],
    "en": ["list", "create", "edit", "view", "delete", "send", "pdf", "recurring", "status", "payments", "reports", "export", "permissions", "credit-note", "templates", "multi-currency", "taxes", "custom-fields"],
    "fr": ["liste", "créer", "éditer", "voir", "supprimer", "envoyer", "pdf", "récurrent", "statut", "paiements", "rapports", "exporter", "autorisations", "note-de-crédit", "modèles", "multi-devise", "impôts", "champs-personnalisés"]
}

# Función para crear el directorio si no existe
def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Crear las carpetas y archivos para cada idioma
for lang, carpeta in idiomas.items():
    base_dir = lang
    facturas_dir = os.path.join(base_dir, carpeta)

    # Crear directorios
    create_dir(facturas_dir)

    # Crear páginas para cada idioma y cada tipo de página
    for pagina in paginas_traducidas[lang]:
        pagina_file = os.path.join(facturas_dir, f"{pagina}.md")
        with open(pagina_file, "w") as f:
            f.write(f"# {pagina.capitalize()}\n")
            f.write(f"Contenido para la página de {pagina} en el idioma {lang}.\n")

    # Crear el archivo sidebar.md para el idioma
    sidebar_file = os.path.join(base_dir, "_sidebar.md")
    with open(sidebar_file, "w") as sidebar:
        sidebar.write("# Introducción\n")
        sidebar.write("  - [Inicio](README.md)\n\n")
        sidebar.write("# Facturas\n")

        # Crear enlaces para cada página
        for pagina in paginas_traducidas[lang]:
            nombre_pagina = pagina.replace("-", " ").capitalize()

            if lang == "es":
                sidebar.write(f"  - [{nombre_pagina}]({lang}/facturas/{pagina}.md)\n")
            elif lang == "en":
                sidebar.write(f"  - [{nombre_pagina}]({lang}/invoices/{pagina}.md)\n")
            else:
                sidebar.write(f"  - [{nombre_pagina}]({lang}/factures/{pagina}.md)\n")

        # Añadir los enlaces de cambio de idioma
        sidebar.write("\n")
        sidebar.write("[🇪🇸 Español](/es) | [🇬🇧 English](/en/) | [🇫🇷 Français](/fr/)\n")

    print(f"Sidebar y carpetas creadas para el idioma {lang}: {sidebar_file}")

print("¡El proceso ha terminado con éxito!")
