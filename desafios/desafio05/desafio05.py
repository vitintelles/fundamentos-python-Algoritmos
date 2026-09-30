def liberar_acesso_sala (status_pagamento, hora_atual):
    if status_pagamento == "pago" and 8 <= hora_atual <= 18:
        return f"Acesso liberado: Comando enviado para fechadura"
    else:
        return f"Acesso negado: Verifique o pagamento ou o horário"

cliente1 = liberar_acesso_sala("pago", 10)
cliente2 = liberar_acesso_sala("pago", 7)
cliente3 = liberar_acesso_sala("Pendente", 16)
cliente4 = liberar_acesso_sala("Pendente", 20)

print(cliente1)
print(cliente2)
print(cliente3)
print(cliente4)