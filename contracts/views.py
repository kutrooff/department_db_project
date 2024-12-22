from django.shortcuts import render, redirect
from .managers import AccessManager
from .models import Client


# чтение всех договоров
def contract_list(request):
    manager = AccessManager()
    contracts = manager.fetch_all()
    manager.close()
    return render(request, 'contracts/list.html', {'contracts': contracts})

# создание нового договора
def contract_create(request):
    if request.method == 'POST':
        monthly_fee = request.POST['monthly_fee']
        effective_date = request.POST['effective_date']
        expiry_date = request.POST['expiry_date']
        client_name = request.POST['client']
        manager = AccessManager()
        client_id = manager.fetch_client_id_by_name(client_name)
        manager = AccessManager()
        manager.create(monthly_fee, effective_date, expiry_date, client_id)
        manager.close()
        return redirect('contract_list')
    manager = AccessManager()
    clients = manager.names_clients()
    manager.close()
    return render(request, 'contracts/create.html', {'clients':clients})

# обновление договора
def contract_update(request, contract_id):
    manager = AccessManager()
    if request.method == 'POST':
        monthly_fee = request.POST['monthly_fee']
        effective_date = request.POST['effective_date']
        expiry_date = request.POST['expiry_date']
        client_name = request.POST['client']
        client_id = manager.fetch_client_id_by_name(client_name)
        manager.update(contract_id, monthly_fee, effective_date, expiry_date, client_id)
        manager.close()
        return redirect('contract_list')
    manager = AccessManager()
    contract = manager.contract_client_information(contract_id)
    clients = manager.names_clients()
    manager.close()
    return render(request, 'contracts/update.html', {'contract_id': contract_id, 'contract': contract, 'clients': clients})

# удаление договора
def contract_delete(request, contract_id):
    if request.method == 'GET':
        manager = AccessManager()
        manager.delete(contract_id)
        manager.close()
        return redirect('contract_list')

