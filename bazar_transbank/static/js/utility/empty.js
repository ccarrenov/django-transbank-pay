function isEmpty(value, name) {
    if (value.length == 0) {
        return "El campo " + name + " debe ser ingresado.\n";
    }
    return "";
}