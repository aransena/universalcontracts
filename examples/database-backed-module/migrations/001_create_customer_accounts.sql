create table customer_accounts (
  id text primary key,
  tenant_id text not null,
  billing_email text not null
);

create table subscriptions (
  id text primary key,
  customer_account_id text not null references customer_accounts(id),
  status text not null
);
