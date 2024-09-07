from django.shortcuts import render,redirect
from django.http import JsonResponse


def payment(request):
    print("Payment View is running")
    if request.method == 'POST':
        payment_id = request.POST['payment_id']
        order_id = request.POST.get('order_id')
        signature = request.POST.get('signature')
        amount = request.POST.get('amount')

        print(payment_id)
        print(order_id)
        print(signature)
        print(amount)

        return redirect("home")

from django.contrib import messages
import razorpay

# def payment(request):
#     if request.method == 'POST':
#         # Access payment data from Razorpay's POST request
#         payment_id = request.POST.get('razorpay_payment_id')
#         order_id = request.POST.get('razorpay_order_id')
#         signature = request.POST.get('razorpay_signature')  # Signature is received automatically

#         # Verify payment signature using Razorpay's server-side library or API
#         # (Replace with your actual Razorpay Key ID and Secret)
#         razorpay_client = razorpay.Client(auth=("rzp_test_YOUR_KEY_ID", "rzp_test_YOUR_SECRET"))

#         try:
#             verification = razorpay_client.utility.verify_payment_signature(
#                 {
#                     'razorpay_order_id': order_id,
#                     'razorpay_payment_id': payment_id,
#                     'razorpay_signature': signature
#                 }
#             )

#             if verification:
#                 # Payment successful! Handle payment processing logic here
#                 # (e.g., update order status, send confirmation email, etc.)
#                 messages.success(request, 'Payment successful!')
#                 # Redirect to a success page or handle further actions
#                 return redirect('success_url')  # Replace with your success URL name
#             else:
#                 messages.error(request, 'Payment verification failed!')
#         except Exception as e:
#             messages.error(request, f'Payment verification error: {e}')

#         return redirect("home")


def payment(request):
    
    return redirect('home')